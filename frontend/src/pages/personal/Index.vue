<template>
    <div class="row justify-center full-height">
        <div draggable="true"
             class="col-lg-5 col-md-5 col-sm-11 col-xs-11 element q-mb-md q-mr-md column justify-center items-center">
            <q-icon name="face" color="warning" size="5rem"/>
            <span class="text-h4 text-white text-uppercase text-weight-bold">About <span class="text-warning">me</span></span>
        </div>
        <div draggable="true"
             class="col-lg-5 col-md-5 col-sm-11 col-xs-11 element q-mb-md q-ml-md column justify-center items-center">
            <q-icon name="view_stream" color="primary" size="5rem"/>
            <span class="text-h4 text-white text-uppercase text-weight-bold">My <span class="text-primary">resume</span></span>
        </div>
        <div draggable="true"
             class="col-lg-5 col-md-5 col-sm-11 col-xs-11 element q-mt-md q-mr-md column justify-center items-center">
            <q-icon name="article" color="positive" size="5rem"/>
            <span class="text-h4 text-white text-uppercase text-weight-bold">My <span
                class="text-positive">portfolio</span></span>
        </div>
        <div draggable="true"
             class="col-lg-5 col-md-5 col-sm-11 col-xs-11 element q-mt-md q-ml-md column justify-center items-center">
            <q-icon name="alternate_email" color="accent" size="5rem"/>
            <span class="text-h4 text-white text-uppercase text-weight-bold">Contact <span class="text-accent">me</span></span>
        </div>
    </div>
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent({
    name: "Index"
})
</script>

<style scoped>
.element {
    background-color: #39354c;
    border-radius: 9px !important;
    transition: background-color .5s, border-radius .5s;
}

.element:hover {
    background-color: #46425e;
    cursor: pointer;
    border-radius: 50px !important;
    transition: background-color .5s, border-radius .5s;
}
</style>
