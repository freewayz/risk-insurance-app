npm install
npm run build
aws s3 cp dist/ s3://britcore-peter/ --recursive
