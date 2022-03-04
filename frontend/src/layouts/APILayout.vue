<template>
    <q-layout view="hHh lpR fFf">
        <q-header class="bg-dark">
            <q-toolbar>
                <q-btn
                    flat
                    round
                    icon="menu"
                    aria-label="Menu"
                    @click="toggleLeftDrawer"
                />
                <q-space />
                <div>
                    <q-btn flat round :icon="getDarkModeIcon()" @click="toggleDarkMode" />
                    <span class="q-ml-md text-overline">V0.0.1a</span>
                </div>
            </q-toolbar>
        </q-header>

        <q-drawer
            v-model="leftDrawerOpen"
            side="left"
        >
            <q-list>
                <q-item-label class="text-bold" header>Accounts</q-item-label>

                <NavigationLink
                    v-for="link in accountsLinks"
                    :key="link.title"
                    v-bind="link"
                />

                <q-item-label class="text-bold" header>APIs</q-item-label>
            </q-list>
        </q-drawer>

        <q-page-container>
            <router-view/>
        </q-page-container>
    </q-layout>
</template>

<script>
const accountsLinks = [
    {
        title: 'Mail',
        caption: 'Tools to deal with Email',
        icon: 'fas fa-envelope',
        link: '/mail'
    },
    {
        title: 'Telegram',
        caption: 'Tools to deal with Telegram',
        icon: 'fab fa-telegram',
        link: '/telegram'
    },
    {
        title: 'Discord',
        caption: 'Tools to deal with Discord',
        icon: 'fab fa-discord',
        link: '/discord'
    },
    {
        title: 'Instagram',
        caption: 'Tools to deal with Instagram',
        icon: 'fas fa-hashtag',
        link: '/instagram'
    },
    {
        title: 'Twitter',
        caption: 'Tools to deal with Twitter',
        icon: 'fab fa-twitter',
        link: '/twitter'
    },
    {
        title: 'Steam',
        caption: 'Tools to deal with Twitter',
        icon: 'fab fa-steam',
        link: '/steam'
    }
];

import {defineComponent, ref} from 'vue'
import {setCssVar, useQuasar} from 'quasar'
import NavigationLink from 'components/NavigationLink.vue'


export default defineComponent({
    name: 'MainLayout',

    components: {
        NavigationLink
    },

    setup() {
        const $q = useQuasar()
        const leftDrawerOpen = ref(false)

        accountsLinks.sort((a, b) => {
            if(a.title < b.title) { return -1; }
            if(a.title > b.title) { return 1; }
            return 0;
        })

        // setCssVar('dark', '#364F6B')
        // setCssVar('primary', '#AA96DA')
        // setCssVar('secondary', '#FCBAD3')
        // setCssVar('accent', '#A8D8EA')

        return {
            accountsLinks: accountsLinks,

            leftDrawerOpen,
            toggleLeftDrawer() {
                leftDrawerOpen.value = !leftDrawerOpen.value
            },
            getDarkModeIcon() {
                return $q.dark.isActive ? 'fas fa-sun' : 'fas fa-moon'
            },
            toggleDarkMode() {
                $q.dark.toggle()
            }
        }
    }
})
</script>
