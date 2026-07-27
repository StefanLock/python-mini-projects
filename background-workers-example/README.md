# Getting started

`Docker compose up --build`

`curl -X POST "http://127.0.0.1:8000/enqueue-task" -H "Content-Type: application/json"      -
d '{"service_name": "k8s-metrics-parser", "status": "failed"}'`