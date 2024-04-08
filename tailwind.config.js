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
          default: "#2CA24D",
        },
        yellow: {
          default: "#F5B10F",
          dark: "#C7A700"
        }
      }
    },
  },
  plugins: [
    require('flowbite/plugin')({
      charts: true,
  })
  ],
}