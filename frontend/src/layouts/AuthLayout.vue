<template>
    <q-layout>

        <q-header class="transparent">
            <q-toolbar class="bg-transparent">
                <q-space />
                <q-btn flat round :icon="getDarkModeIcon()" @click="toggleDarkMode" :color="getDarkModeIconColor()" />
                <span class="q-ml-md text-overline" :class="'text-' + getDarkModeIconColor()">V0.0.1a</span>
            </q-toolbar>
        </q-header>

        <q-page-container>
            <router-view/>
        </q-page-container>
    </q-layout>
</template>

<script>
import {useQuasar} from "quasar";

export default {
    name: "AuthLayout",
    setup() {
        const $q = useQuasar()
        return {
            getDarkModeIcon() {
                return $q.dark.isActive ? 'fas fa-sun' : 'fas fa-moon'
            },
            toggleDarkMode() {
                $q.dark.toggle()
            },
            getDarkModeIconColor() {
                return $q.dark.isActive ? 'white' : 'black'
            }
        }
    }
}
</script>

<style scoped>

</style>
