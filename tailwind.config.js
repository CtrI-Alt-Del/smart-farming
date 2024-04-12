/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/ui/templates/**/*.html', './src/ui/static/src/**/*.js'],
  theme: {
    extend: {
      colors: {
        header: {
          background: "#1F2A37"
        },
        green: {
          default: '#D3F7EB',
        },
        yellow: {
          default: '#FDF6B2',
          dark: '#FDF6B2',
        },
      },
    },
  },
  plugins: [
    require('flowbite/plugin')({
      charts: true,
    }),
    require('tailwindcss-animated')
  ],
}
