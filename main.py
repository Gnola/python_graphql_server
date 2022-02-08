from graphene import ObjectType, String, Schema, Int

class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"), age=Int())

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name, age):
        return f'Hello {name} you are {age}!'


def main():
    schema = Schema(query=Query)
    result = schema.execute('{hello(name: "G", age: 13)}')
    print(result.data['hello'])

# If imported it WONT run main()
if __name__ == '__main__':
    main()
