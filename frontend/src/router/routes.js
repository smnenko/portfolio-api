
const routes = [
  {
    path: '/api',
    component: () => import('layouts/APILayout.vue'),
    children: [
      { path: '/api/', component: () => import('pages/api/Index.vue') },
      { path: '/api/discord', component: () => import('pages/api/Discord.vue') },
    ]
  },

  {
    path: '/',
    component: () => import('layouts/PortfoliolLayout.vue'),
    children: [
      { path: '/', component: () => import('pages/portfolio/Index.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/api/Error404.vue')
  }
]

export default routes
