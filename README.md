# graphql-example
Simple example of creating a graphql schema on top of a simple REST service

**This repository has 2 branches**
1. main --> A simple REST service with basic operations, one in Flask `app.py` and one in Spring Boot `demo`
2. graphql --> The same service in main, but with added GraphQL schemas, built with [Graphene](https://graphene-python.org/)/[flask-graphql](https://github.com/graphql-python/flask-graphql) and [Netflix DGS](https://netflix.github.io/dgs/) respectively

Hope it's useful!

### Base endpoints
Flask service: `localhost:8081`<br>
Spring Boot service: `localhost:8080`

#### Get
`/products`<br>
`/brands`

#### Post
`/brand`<br>
Add a brand. Accepts a body with brand attributes:
1. name _String_
2. description _String_
3. hq _String_
