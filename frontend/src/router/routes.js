
const routes = [
  {
    path: '/api',
    component: () => import('layouts/APILayout.vue'),
    children: [
      { path: '/api/', component: () => import('pages/api/Index.vue') },
      { path: '/api/discord', component: () => import('pages/api/Discord.vue') },
      { path: '/api/mail', component: () => import('pages/api/Mail.vue') },
    ]
  },

  {
    path: '/',
    component: () => import('layouts/PortfolioLayout.vue'),
    children: [
      { path: '/', component: () => import('pages/portfolio/Index.vue') }
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
