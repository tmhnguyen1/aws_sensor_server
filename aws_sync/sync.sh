#!/bin/bash

AWS_CLI_PATH="/usr/local/bin/aws"
echo "$(date) Log sync entry" >> /app/data/synclog.log
$AWS_CLI_PATH s3 sync /app/data/data_csv s3://lalamove-apas/counter/test_counter --region ap-east-1