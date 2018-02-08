cd client
npm run build
workon devops
export AWS_PROFILE=abole
aws s3 cp dist/ s3://britcore-peter/ --recursive
aws s3 cp secret-config.json 