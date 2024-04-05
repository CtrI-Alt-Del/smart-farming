/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/ui/templates/**/*.html",
    "./src/ui/static/src/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin")
  ],
}