<script>

import {defineComponent} from "vue";
import {useQuasar} from "quasar";

export default defineComponent({
    name: "SignOut",
    mounted() {
        if (!this.$q.cookies.has('token')) {
            this.$router.push('/api')
        } else {
            this.$q.cookies.remove('token')
            this.$router.push('/api')
        }
    }
})

</script>
