import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Register from '../pages/Register.vue'
import Login from '../pages/Login.vue'
import Profile from '../pages/Profile.vue'
import ProfileFake from '../pages/ProfileFake.vue'
import Tasks from '../pages/Tasks.vue'
import End from '../pages/end.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/register', name: 'Register', component: Register },
    { path: '/login', name: 'Login', component: Login },
    { path: '/profile', name: 'Profile', component: Profile },
    { path: '/profi1e', name: 'ProfileFake', component: ProfileFake },
    { path: '/tasks', name: 'Tasks', component: Tasks },
    { path: '/end', name: 'End', component: End },
  ]
})

export default router
