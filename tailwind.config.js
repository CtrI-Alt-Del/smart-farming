/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/ui/templates/**/*.html",
    "./src/ui/static/src/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        green: {
          default: "##2CA24D",
        },
      }
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
}