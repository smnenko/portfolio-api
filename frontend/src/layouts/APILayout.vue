<template>
  <q-layout view="lHh lpR fFf">
    <q-header>
      <q-toolbar class="bg-dark">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title class="animated">
          smnenko
        </q-toolbar-title>

        <div>V0.0.1a</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      class="bg-grey-10"
      side="left"
      show-if-above
    >
      <q-list>

        <q-item-label class="text-bold" header>Accounts</q-item-label>

        <NavigationLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />

        <q-item-label class="text-bold" header>APIs</q-item-label>

      </q-list>

      <q-btn label="Logout" unelevated color="grey-15" class="text-uppercase full-width" />
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import NavigationLink from 'components/navigation/NavigationLink.vue'

const linksList = [
  {
    title: 'Home',
    caption: 'Return to the home page',
    icon: 'home',
    link: '/'
  },
  {
    title: 'Telegram',
    caption: 'Tools to deal with Telegram',
    icon: 'telegram',
    link: '/telegram'
  },
  {
    title: 'Discord',
    caption: 'Tools to deal with Discord',
    icon: 'discord',
    link: '/discord'
  },
  {
    title: 'Instagram',
    caption: 'Tools to deal with Instagram',
    icon: 'send',
    link: '/instagram'
  },
  {
    title: 'Twitter',
    caption: 'Tools to deal with Twitter',
    icon: 'tag',
    link: '/twitter'
  }
];

import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
    NavigationLink
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>
