<template>
    <q-item
        clickable
        :to="'/api' + link"
        class="q-py-md"
        active-class="text-secondary"
    >
        <q-item-section
            v-if="icon"
            avatar
        >
            <q-icon right :name="icon" color="secondary"/>
        </q-item-section>

        <q-item-section>
            <q-item-label>{{ title }}</q-item-label>
            <q-item-label caption>
                {{ caption }}
            </q-item-label>
        </q-item-section>
    </q-item>
</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
    name: 'EssentialLink',
    props: {
        title: {
            type: String,
            required: true
        },

        caption: {
            type: String,
            default: ''
        },

        link: {
            type: String,
            default: '#'
        },

        icon: {
            type: String,
            default: ''
        }
    }
})
</script>
