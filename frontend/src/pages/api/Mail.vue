<template>
    <q-page class="column q-mx-sm">
        <div class="row full-width q-my-sm">
            <q-card bordered class="col-lg col-md col-sm col-xs-12 q-ma-sm text-center q-my-sm">
                <q-card-section>
                    <div class="text-overline">Accounts created today:</div>
                    <div class="text-h2">0</div>
                </q-card-section>
            </q-card>
            <q-card bordered class="col-lg col-md col-sm col-xs-12 q-ma-sm text-center q-my-sm">
                <q-card-section>
                    <div class="text-overline">Accounts created last week:</div>
                    <div class="text-h2">0</div>
                </q-card-section>
            </q-card>
            <q-card bordered class="col-lg col-md col-sm col-xs-12 q-ma-sm text-center q-my-sm">
                <q-card-section>
                    <div class="text-overline">Accounts created at all:</div>
                    <div class="text-h2">0</div>
                </q-card-section>
            </q-card>
        </div>

        <q-table
            :columns="columns"
            :rows="rows"
            selection="multiple"
            v-model:selected="selected"
            row-key="id"
            :rows-per-page-options="[5, 10, 15, 20, 0]"
            bordered
            class="q-mx-sm"
        />

        <div class="flex q-mt-md justify-end">
            <q-btn flat rounded color="secondary" label="Create" class="q-mx-sm" />
            <q-btn flat rounded color="negative" label="Delete" class="q-mx-sm" @click="deleteRecords" />
            <q-btn flat rounded color="warning" label="Clear" class="q-mx-sm" @click="clearTableSelection" />
            <q-btn-dropdown flat rounded color="accent" label="Export" class="q-mx-sm">
                <q-list>
                    <q-item clickable v-close-popup>
                        <q-item-section>
                            <q-avatar icon="fas fa-file" />
                        </q-item-section>
                        <q-item-section>
                            <q-item-label>TXT</q-item-label>
                        </q-item-section>
                    </q-item>
                    <q-item clickable v-close-popup>
                        <q-item-section>
                            <q-avatar icon="fas fa-file-pdf" />
                        </q-item-section>
                        <q-item-section>
                            <q-item-label>PDF</q-item-label>
                        </q-item-section>
                    </q-item>
                    <q-item clickable v-close-popup>
                        <q-item-section>
                            <q-avatar icon="fas fa-file-csv" />
                        </q-item-section>
                        <q-item-section>
                            <q-item-label>CSV</q-item-label>
                        </q-item-section>
                    </q-item>
                </q-list>
            </q-btn-dropdown>
        </div>

    </q-page>
</template>

<script>
import {defineComponent, ref} from "vue";

const columns = [
    {name: 'emails', required: true, label: 'Email', align: 'left', field: row => row.email, sortable: true},
    {name: 'passwords', required: true, label: 'Password', align: 'left', field: row => row.password, sortable: false},
    {name: 'secrets', required: true, label: 'Secret answer', align: 'left', field: row => row.secret, sortable: false}
]

const rows = [
    {id: 0, email: 'stanichgame@gmail.com', password: 'qwerty12345', secret: '3213'},
    {id: 1, email: 'semenenkostanich@mail.ru', password: 'qwerty12345', secret: '3213'},
    {id: 2, email: 'mmsstt@mail.ru', password: 'qwerty12345', secret: '3213'}
]

export default defineComponent ({
    name: "Mail",
    methods: {
        clearTableSelection: function (event) {
            this.selected = []
        },
        deleteRecords: function (event) {
            alert('Records has been deleted')
        }
    },
    setup() {
        const selected = ref([])

        return {
            columns: columns,
            rows: rows,
            selected: selected,
        }
    }
})
</script>

<style scoped>

</style>
