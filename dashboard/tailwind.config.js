/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'header-carnet': "url('/src/assets/img/bg-header.svg')",
        'cuadricula': "url('/src/assets/img/cuadricula.jpg')",
      },
      colors: {
        orangecpv: {
          100: "#ffe2cc",
          200: "#ffc599",
          300: "#ffa766",
          400: "#ff8a33",
          500: "#ff6d00",
          600: "#cc5700",
          700: "#994100",
          800: "#662c00",
          900: "#331600"
        },
        cyancpv: {
          100: "#d7f2ee",
          200: "#aee4de",
          300: "#86d7cd",
          400: "#5dc9bd",
          500: "#01A088",
          600: "#2a968a",
          700: "#207167",
          800: "#154b45",
          900: "#0b2622"
        },
        add: {
          100: '#e1fdcf',
          200: '#c3fc9e',
          300: '#a6fa6e',
          400: '#88f93d',
          500: '#6af70d',
          600: '#55c60a',
          700: '#409408',
          800: '#2a6305',
          900: '#153103',
        },
        primary: {
          100: '#d7f0ff',
          200: '#99e3e3',
          300: '#66d4d5',
          400: '#33c6c7',
          500: '#00b8b9',
          600: '#009394',
          700: '#006e6f',
          800: '#004a4a',
          900: '#002525',
        },
        secondary: {
          100: '#cce9fe',
          200: '#99d3fe',
          300: '#66bcfd',
          400: '#33a6fd',
          500: '#0090fc',
          600: '#0073ca',
          700: '#005697',
          800: '#003a65',
          900: '#001d32',
        },
        light: {
          100: '#f5f5f5',
          200: '#e7e7e7',
          300: '#dadada',
          400: '#cecece',
          500: '#c2c2c2',
          600: '#9b9b9b',
          700: '#747474',
          800: '#4e4e4e',
          900: '#272727',
        },
        dark: {
          100: '#dadbdd',
          200: '#b5b6ba',
          300: '#8f9298',
          400: '#6a6d75',
          500: '#454953',
          600: '#373a42',
          700: '#292c32',
          800: '#1c1d21',
          900: '#0e0f11',
        },


      },
    },
  },
  plugins: [],
}