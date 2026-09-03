apiVersion: apps/v1       # Which API?
kind: Deployment           # What?

metadata:
  name: pathnex-deployment # Name?

spec:
  replicas: 2              # How many Pods?

  selector:                # Which Pods?
    matchLabels:
      app: pathnex-app

  template:                # How to create Pods?
    metadata:
      labels:               # Pod identity
        app: pathnex-app

    spec:                   # What runs inside Pod?
      containers:
        - name: app         # Name
          image: nginx      # Image
          ports:
            - containerPort: 80  # Port