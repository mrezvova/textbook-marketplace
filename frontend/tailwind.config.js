   /* @type {import('tailwindcss').Config} */
   module.exports = {
    content: [
    "./**/.{js,ts,jsx,tsx}", // Note the addition of the app directory.
    "./src/pages/*.{js,ts,jsx,tsx,html,vue}",
    "./src/components/*.{js,ts,jsx,tsx,html,vue}",
    ".src/App.vue",
    ],
    theme: {
      extend: {},
    },
  };
  
