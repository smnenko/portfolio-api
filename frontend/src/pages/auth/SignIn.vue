<template>
    <q-page class="flex flex-center">
        <q-form class="text-center" style="max-width: 24rem; width: 24rem" @submit="onSubmit">
            <div class="text-left text-h4">Sign in</div>
            <div class="text-left text-caption q-mb-sm">Stay updated on our awesome service</div>

            <q-input label="Username" model-value="" class="q-my-sm" color="secondary" v-model="username"/>
            <q-input label="Password" model-value="" class="q-my-sm" color="secondary" v-model="password"
                     :type="isPassword ? 'password' : 'text'">
                <template v-slot:append>
                    <q-icon class="cursor-pointer" :name="isPassword ? 'far fa-eye' : 'far fa-eye-slash'"
                            @click="isPassword = !isPassword"/>
                </template>
            </q-input>
            <div class="text-left q-my-sm">
                <router-link class="text-left text-secondary" to="/api/recover-password" style="text-decoration: none">
                    Forgot password?
                </router-link>
            </div>
            <q-btn rounded color="secondary" type="submit" class="text-bold full-width q-my-sm" label="Sign in"/>
            <div class="q-my-sm">New to our service?
                <router-link class="text-secondary text-bold" to="/api/signup" style="text-decoration: none">Join now
                </router-link>
            </div>
        </q-form>
    </q-page>
</template>

<script>
import {defineComponent, ref} from "vue";
import gql from "graphql-tag";
import {useMutation} from "@vue/apollo-composable";


export default defineComponent({
    name: "SignIn",
    methods: {
        onSubmit: function (e) {
            e.preventDefault()
            this.authenticate().then(
                (response) => {
                    const {token, payload, refreshExpireIn} = response.data['tokenAuth']
                    this.$q.cookies.set('token', token, {expires: refreshExpireIn})
                    this.$q.cookies.set('username', payload['username'], {expires: refreshExpireIn})
                    this.$router.push('/api')
                }
            )
        }
    },
    mounted() {
        if (this.$q.cookies.has('token')) {
            this.$router.push('/api')
        }
    },
    setup() {
        const isPassword = ref(true)
        const username = ref(null)
        const password = ref(null)
        const {mutate: authenticateMutation} = useMutation(gql`mutation
            tokenAuth($username: String!, $password: String!) {
                tokenAuth(username: $username, password: $password) {
                    token
                    payload
                    refreshExpiresIn
                }}`, () => ({
            variables: {
                username: username.value,
                password: password.value
            }
        }))

        return {
            isPassword: isPassword,
            username: username,
            password: password,

            authenticate: authenticateMutation
        }
    }
})
</script>
