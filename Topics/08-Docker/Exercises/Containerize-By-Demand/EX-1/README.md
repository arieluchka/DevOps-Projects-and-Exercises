## Containerize a ToDo app
This is a simple ToDo web application that uses HTML, CSS, and JavaScript. Users can add tasks, mark tasks as completed, and clear completed tasks.

Your task is to containerize this application, including all of it's dependencies, so anyone will be able to `docker run -p 8080:8080 todo-app:1.0` and see the Web App.

**Copy this whole folder exercise to your local computer.**

The folder `todo-app` has 3 files. All of this files need to be **in the same directory** in the container, for the application to work.

The application **uses `node.js`** runtime and the **`http-server` package**, and will run on **port 8080**.

Try to complete the exercise with the minimal information above. You **have** to search the internet to understand what you need and how to implement, but please, **Do not use chatGPT to get a quick answer**. 
The whole point of this exercise is to practice researching and how to handle unknow areas.

---

Build and test your images and see how every change you do to the Dockerfile affects the build.

---

### HINTS
You can use the Hints below for basic guidelines and steps you need to take.
**Start with the small hints, just to get some directions.**
If you are still stuck, procceed to the big hints.
You can also look at the Answer at the bottom.


##### Small hints

<details>
  <summary>Where to start</summary>

First, Try to understand what dependencies you have to intsall. The app needs `nodejs` and needs the `http-server` **package**. 

Is there already a docker image with these dependencies that you can use? 
If you dont want to base yours on another image, how can you install `nodejs` and `http-server` on your own image?
(`http-server` is a package, so we need some sort of **package manager** to be able to install it...)
</details>

<details>
  <summary>How to run the application</summary>
  
The application uses **http-server** package. You need to figure out what http-server command you need to run this application on port 8080. Then, you can enter it in the `CMD` line in your Dockerfile.
</details>

##### Big hints
<details>
  <summary>How to get dependencies - part 1</summary>

one way to get node.js is to base your image on [the official node docker image](https://hub.docker.com/_/node).

For example:
`FROM node:14` 

To install the **http-server** package, you would need to use the **npm package manager**, which already comes with the node image (npm for JS is like pip for python).

Try to figure out by yourself, how to use **npm** to install **http-server**.
</details>

<details>
  <summary>How to get dependencies - part 2</summary>

To install the `http-server` package, using the `npm` package manager, you can use:

`RUN npm install -g http-server`
(-g flag is to install the package **globally**, so it can be used from anywhere in the container.)
</details>

<details>
  <summary>The CMD command to run the application</summary>

To run the application with `http-server` on port 8080 you would need to add:
`CMD ["http-server", ".", "-p", "8080"]`
</details>


##### Answer
<details>
  <summary>Final answer</summary>

Dockerfile:

```
FROM node:14

WORKDIR /usr/src/app

COPY ./todo-app/ .

RUN npm install -g http-server

EXPOSE 8080

CMD ["http-server", ".", "-p", "8080"]
```

from the directory with the dockerfile, run the command:
`docker build -t todo-app .`

To run:
`docker run -p 8080:8080 todo-app`
</details>