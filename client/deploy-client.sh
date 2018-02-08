npm run build
export AWS_PROFILE=abole
aws s3 cp dist/ s3://britcore-peter/ --recursive