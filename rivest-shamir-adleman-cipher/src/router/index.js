import { createRouter, createWebHistory } from 'vue-router'

import encrypt from '@/components/encrypt.vue'
import decrypt from '@/components/decrypt.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: "/encrypt", component: encrypt},
    {path: "/decrypt", component: decrypt}
  ],
})

export default router
