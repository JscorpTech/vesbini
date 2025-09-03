pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    environment {
        TEST_ENV     = "/opt/env/.env.test.vesbini"
        PROD_ENV     = "/opt/env/.env.vesbini"
        IMAGE_NAME   = "vesbini"
        TEST_TAG     = "test"
        PROD_TAG     = "latest"
        CONTAINER_DB = "vesbini_db_test"
        CONTAINER_WEB = "vesbini_web_test"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', credentialsId: 'ssh', url: 'git@github.com:JscorpTech/vesbini.git'
            }
        }

        stage('Build Test Image') {
            steps {
                sh """
                    cp ${TEST_ENV} ./.env
                    docker build -t ${IMAGE_NAME}:${TEST_TAG} .
                """
            }
        }

        stage('Start Test DB') {
            steps {
                sh """
                    docker run -d --rm --name ${CONTAINER_DB} -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=testdb -p 5433:5432 postgres:15
                    echo "⏳ Waiting for database..."
                    for i in {1..30}; do
                        if docker exec ${CONTAINER_DB} pg_isready -U postgres >/dev/null 2>&1; then
                            echo "✅ Database ready"
                            break
                        fi
                        echo "Database not ready yet... retrying..."
                        sleep 2
                    done
                """
            }
        }

        stage('Run Migrations & Tests') {
            steps {
                sh """
                    docker run --rm --name ${CONTAINER_WEB} --link ${CONTAINER_DB}:db \
                        -e DATABASE_HOST=db \
                        -e DATABASE_PORT=5432 \
                        -e DATABASE_USER=postgres \
                        -e DATABASE_PASSWORD=postgres \
                        -e DJANGO_SETTINGS_MODULE=config.settings.test \
                        ${IMAGE_NAME}:${TEST_TAG} \
                        sh -c "python manage.py migrate && pytest -v"
                """
            }
        }

        stage('Build Production Image') {
            when {
                expression { currentBuild.currentResult == "SUCCESS" }
            }
            steps {
                sh """
                    cp ${PROD_ENV} ./.env
                    docker build -t ${IMAGE_NAME}:${PROD_TAG} .
                """
            }
        }
    }

    post {
        always {
            sh "docker stop ${CONTAINER_DB} || true"
            echo "Pipeline finished: ${currentBuild.currentResult}"
        }

        success {
            withCredentials([
                string(credentialsId: 'bot-token', variable: 'BOT_TOKEN'),
                string(credentialsId: 'chat-id', variable: 'CHAT_ID')
            ]) {
                sh '''
                curl -s -X POST https://api.telegram.org/bot${BOT_TOKEN}/sendMessage \
                -d chat_id=${CHAT_ID} \
                -d text="✅ SUCCESS: ${JOB_NAME} #${BUILD_NUMBER}"
                '''
            }
        }

        failure {
            withCredentials([
                string(credentialsId: 'bot-token', variable: 'BOT_TOKEN'),
                string(credentialsId: 'chat-id', variable: 'CHAT_ID')
            ]) {
                sh '''
                curl -s -X POST https://api.telegram.org/bot${BOT_TOKEN}/sendMessage \
                -d chat_id=${CHAT_ID} \
                -d text="🚨 FAILED: ${JOB_NAME} #${BUILD_NUMBER}"
                '''
            }
        }
    }
}
