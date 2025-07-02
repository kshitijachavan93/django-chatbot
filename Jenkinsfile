pipeline {
  agent any

  environment {
    AWS_REGION = "eu-north-1" 
    IMAGE_TAG = "${BUILD_NUMBER}"
    ECR_REPO = "486991249421.dkr.ecr.eu-north-1.amazonaws.com/django-chatbot" 
  }

  stages {
    stage('Build Docker Image') {
      steps {
        sh "docker build -t django-chatbot:${IMAGE_TAG} ."
      }
    }

    stage('Push Image to ECR') {
      steps {
        sh '''
          aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}
          docker tag django-chatbot:${IMAGE_TAG} ${ECR_REPO}:${IMAGE_TAG}
          docker push ${ECR_REPO}:${IMAGE_TAG}
        '''
      }
    }

    stage('Register ECS Task') {
      steps {
        sh '''
          sed "s|<IMAGE_TAG>|${IMAGE_TAG}|g" task-def.json > new-task-def.json

          aws ecs register-task-definition \
            --cli-input-json file://new-task-def.json
        '''
      }
    }

    stage('Deploy to ECS') {
      steps {
        sh '''
          aws ecs update-service \
            --cluster django-chatbot-cluster \
            --service django-chatbot-service \
            --region ${AWS_REGION} \
            --force-new-deployment
        '''
      }
    }
  }
}
