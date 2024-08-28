import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  preview: {              
    strictPort: true,
    port: 5173,
  } ,
  server:{
    port: 5173,
    strictPort: true,
    host: true,
    origin: "http://localhost:5173"
  },
  warmup: {
    clientFiles: ['./src/components/*.vue', './src/utils/big-utils.js'],
    ssrFiles: ['./src/server/modules/*.js'],
  }
})
