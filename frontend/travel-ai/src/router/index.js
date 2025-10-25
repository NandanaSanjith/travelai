import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import SuccessPage from '../components/SuccessPage.vue'
import CancelPage from '../components/CancelPage.vue'

// Define custom routes
const routes = [
  {
    path: '/',              // Default route
    name: 'Home',
    component: HomePage
  },
  {
    path: '/success',              // Default route
    name: 'Success',
    component: SuccessPage,
    props: route => ({
      bookingId: route.query.booking_id,
    }),
  },
   {
    path: '/cancel',              // Default route
    name: 'Cancel',
    component: CancelPage,
    props: route => ({
      bookingId: route.query.booking_id,
    }),
  },
  
]

// Create router instance
const router = createRouter({
  history: createWebHistory(),  // Use HTML5 history mode
  routes
})

export default router
