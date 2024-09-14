/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./blueprints/**/*.html",
    "./static/**/*.js",
    "node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#1e3a8a', // A nice blue color
          light: '#3b82f6',
          dark: '#1e40af',
        },
      },
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}

