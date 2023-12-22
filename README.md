
# 📈 Financial Tracker
The primary objective of this project is to facilitate budget management using free and open-source software. Initially, the application will be entirely based in the terminal for testing purposes. In subsequent versions, I intend to create a user-friendly GUI and ultimately develop a web application. My belief is that having access to the application from any device will make it simpler to manage one's budget effectively.

## 👌 About Me
Hello there! I'm currently a second-year cybersecurity student at Wrocław University of Technology.
Recently, I became intrigued by the world of investing, but like many people, I am wary of entrusting my data to large tech companies (which ruled out other investment tracking applications). As a result, I took it upon myself to create a small-scale tracker application to assist with managing my investments. Given that I'm still a student, I opted to begin with personal budget management.

### Installing dependencies
1. Install Tailwind CSS `npm install -D tailwindcss`
2. Initialize Tailwind CSS `npx tailwindcss init`
4. Install Flowbite `npm install flowbite`
5. Configure tailwind.config.js 
```
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./blueprints/**/*.html",
    "./static/**/*.js",
    "node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin")
  ],
}
```
6. Run to compile and watch for changes `npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch`
7. Run main.py to access the application on `localhost:5000`