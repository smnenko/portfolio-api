
const routes = [
  {
    path: '/api',
    component: () => import('layouts/APILayout.vue'),
    children: [
      { path: '/api/', component: () => import('pages/Index.vue') },
      { path: '/api/discord', component: () => import('pages/Discord.vue') },
    ]
  },

  {
    path: '/',
    component: () => import('layouts/PersonalLayout.vue'),
    children: [
      { path: '/', component: () => import('pages/personal/Index.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
