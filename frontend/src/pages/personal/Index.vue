<template>
    <div class="full-height mdi-wrap-disabled">
        <q-tabs class="row justify-center" :class="[this.is_panel ? '' : 'full-height']" v-model="tab" indicator-color="transparent">
            <q-tab draggable="true" name="about" :class="[this.is_panel ? 'hidden' : '']" @click="swap_blocks"
                   class="col-lg-5 col-md-5 col-sm-11 col-xs-11 element q-mb-md q-mr-md column justify-center items-center">
                <q-icon name="face" color="warning" size="5rem"/>
                <span class="text-h4 text-white text-uppercase text-weight-bold">About <span class="text-warning">me</span></span>
            </q-tab>
            <q-tab draggable="true" name="resume" :class="[this.is_panel ? 'hidden' : '']" @click="swap_blocks"
                   class="col-lg-5 col-md-5 col-sm-11 col-xs-11 element q-mb-md q-ml-md column justify-center items-center">
                <q-icon name="view_stream" color="primary" size="5rem"/>
                <span class="text-h4 text-white text-uppercase text-weight-bold">My <span class="text-primary">resume</span></span>
            </q-tab>
            <q-tab draggable="true" name="portfolio" :class="[this.is_panel ? 'hidden' : '']" @click="swap_blocks"
                   class="col-lg-5 col-md-5 col-sm-11 col-xs-11 element q-mt-md q-mr-md column justify-center items-center">
                <q-icon name="article" color="positive" size="5rem"/>
                <span class="text-h4 text-white text-uppercase text-weight-bold">My <span
                    class="text-positive">portfolio</span></span>
            </q-tab>
            <q-tab draggable="true" name="contact" :class="[this.is_panel ? 'hidden' : '']" @click="swap_blocks"
                   class="col-lg-5 col-md-5 col-sm-11 col-xs-11 element q-mt-md q-ml-md column justify-center items-center">
                <q-icon name="alternate_email" color="accent" size="5rem"/>
                <span class="text-h4 text-white text-uppercase text-weight-bold">Contact <span class="text-accent">me</span></span>
            </q-tab>
        </q-tabs>

        <q-tab-panels class="full-height bg-transparent text-white" v-model="tab" :class="[this.is_panel ? '' : 'hidden']">
            <q-tab-panel name="about">
                <q-btn rounded class="absolute-top-right" @click="swap_blocks">
                    Close <q-icon name="close"></q-icon>
                </q-btn>
                <div class="text-h6 flex content-center flex-center full-height" style="letter-spacing: 0.2rem">
                    <table>
                        <tbody>
                            <tr>
                                <td class="text-right text-grey text-overline q-pr-sm">Name</td>
                                <td class="q-pl-sm" style="border-left: 1px solid rgb(255, 148, 114)">Stanislav</td>
                            </tr>
                            <tr>
                                <td class="text-right text-grey text-overline q-pr-sm">Specialization</td>
                                <td class="q-pl-sm" style="border-left: 1px solid rgb(255, 148, 114)">Software Engineer <span class="text-caption">(1.5 years)</span></td>
                            </tr>
                            <tr>
                                <td class="text-right text-grey text-overline q-pr-sm">Passion</td>
                                <td class="q-pl-sm" style="border-left: 1px solid rgb(255, 148, 114)">Refactoring legacy code</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </q-tab-panel>

            <q-tab-panel name="resume">
                <q-btn rounded class="absolute-top-right" @click="swap_blocks">
                    <q-icon name="close" />
                </q-btn>
            </q-tab-panel>

            <q-tab-panel name="portfolio">
                <q-btn rounded class="absolute-top-right" @click="swap_blocks">
                    <q-icon name="close" />
                </q-btn>
            </q-tab-panel>

            <q-tab-panel name="contact">
                <q-btn rounded class="absolute-top-right" @click="swap_blocks">
                    <q-icon name="close" />
                </q-btn>
            </q-tab-panel>
        </q-tab-panels>
    </div>
</template>

<script>
import {defineComponent, ref} from "vue";

export default defineComponent({
    name: "Index",
    setup() {
        return {
            tab: 'main',
            is_panel: ref(false)
        }
    },
    mounted() {
        this.delete_classes()
    },
    methods: {
        delete_classes: function () {
            let el = document.getElementsByClassName('q-tabs__content')[0]
            el.classList.remove('no-wrap')
        },

        swap_blocks: function () {
            this.is_panel = this.is_panel !== true;
        },
    }
})
</script>

<style scoped>

.dark {
    background-color: #262333;
}

.element {
    background-color: #39354c;
    border-radius: 9px !important;
    transition: border-radius .5s;
}

.q-tabs__content {
    flex-wrap: initial !important;
}

.element:hover {
    border-radius: 50px !important;
    transition: border-radius .5s;
}
</style>
