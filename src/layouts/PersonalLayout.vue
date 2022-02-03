<template>
    <q-layout class="fullscreen background">
        <transition appear duration="1000" enter-active-class="animated pulse" leave-active-class="animated fadeOut">
            <div class="fullscreen wrapper dark row q-ma-lg">

                <div class="col-1 row justify-center items-center mobile-hide">
                    <transition appear duration="1000" enter-active-class="animated fadeIn"
                                leave-active-class="animated fadeOut">
                        <div
                            class="text-h5 text-white text-no-wrap text-uppercase text-weight-bold"
                            style="transform: rotate(-90deg); letter-spacing: 20px"
                        >
                            My <span class="text-warning">personal page</span>
                        </div>
                    </transition>
                </div>

                <div class="col-8 column justify-around">
                    <div class="col-2 column justify-center items-center">
                        <div class="text-white text-h2 text-weight-bold text-uppercase" style="letter-spacing: 1rem">
                            Hello I'm <span style="color: #ff9472">Stanislav</span>
                        </div>
                        <div class="text-white text-overline text-weight-bold text-uppercase mobile-hide"
                             style="letter-spacing: 1rem">
                            As a <span style="color: #ff9472">Python Developer</span>
                        </div>
                    </div>

                    <q-page-container class="col-10 q-pb-lg">
                        <router-view/>
                    </q-page-container>
                </div>

                <div class="col-3 column justify-center items-center">

                </div>
            </div>
        </transition>
    </q-layout>
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
    name: "PersonalLayout",
})
</script>

<style scoped>
.background {
    background: linear-gradient(45deg, #ffff99, #ff66ff);
}

.wrapper {
    border-radius: 9px !important;
}

.dark {
    background-color: #262333;
}
</style>
