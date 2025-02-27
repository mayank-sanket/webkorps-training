# Implementing JWT 

# JWT Overview

- JWT is a self-contained way to securely transmit data and information between 
two parties using JSON Object.
-JWT can be trusted because each JWT can be digitally signed, which in return allows the server to know if the JWT has been changed at all
- JWT should be used when dealing with authorization

- JWT is a great way for information to be exchanged between the server and client
- Once a user logs in, the server will return a JWT (which is a string of characters) that when decoded, shows information about the client and the user
- Each time the request comes from the same client after successful authentication, the client will send the JWT and the server will validate the token after each request



# JWT Strucutre

- A JWT is created of three separate parts separated by dots(.) which include : 
            1. Header(a)
            2. Payload(b)
            3. Signature(c)
            aaaaaaaaa.bbbbbbbb.cccccccc


    - A JWT header usually consists of two parts:
            a. "alg": the algorithm for signing
            b. "typ" : the specific type of token

- A JWT header is then encoded using Base64 to create the first JWT (a)

- A JWT payload consists of the data. The payloads data contains claims, and there are 3 kinds of claims
        - registered
        - public 
        - private

- The JWT payload is then encoded using Base64 to create the second part of the JWT (b)




- JWT Signature : the third and the final part of the JWT
- A JWT signature is created by using the algorithm in the header to hash out the encoded header, encoded payload with a secret
- The secret can be anything but is saved somewhere on the server that the client does not have access to
- The signature is the third and the final part of the JWT (c)


# JWT Example

 - JWT Header

  ```
        {
                "alg": "HS256",
                "typ": "JWT"
        }
  ```


- JWT Payload 

```
        {
                "sub": "1234567890",
                "name": "Mayank Sanket",
                "given_name": "Mayank",
                "family_name": "Sanket",
                "email": "mayanksanket@gmail.com",
                "admin": true
        }

```


- JWT Signature
```
    {
        HMACSHA256(
                base64UrlEncode(header) + "." + 
                base64UrlEncode(payload),
                learnonlinesecret)
    }
```


- JWT string for that look like : eydfdfdfdkfjk39urjj. dkfjdklfjkdfjldfjd.fer33434343jkjf 

- the client should not have access to the secret key























        