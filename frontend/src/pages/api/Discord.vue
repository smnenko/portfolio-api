<template>
    <q-page class="column q-mx-md">
        <div class="row full-width q-mt-md q-mb-md">
            <q-card bordered class="col-lg col-xs-12 text-center q-mr-sm">
                <q-card-section>
                    <div class="text-overline">Accounts created today:</div>
                    <div class="text-h2">0</div>
                </q-card-section>
            </q-card>
            <q-card bordered class="col-lg col-xs-12 text-center q-ml-md q-mr-sm">
                <q-card-section>
                    <div class="text-overline">Accounts created last week:</div>
                    <div class="text-h2">0</div>
                </q-card-section>
            </q-card>
            <q-card bordered class="col-lg col-xs-12 text-center q-ml-md">
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
        />

        <div class="flex q-mt-md justify-end">
            <q-btn flat rounded color="secondary" label="Create" class="q-mx-sm" />
            <q-btn flat rounded color="negative" label="Delete" class="q-mx-sm" @click="confirmDelete = true" />
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

        <div class="row q-mt-md">
            <q-card class="col-lg col-xs-12 q-my-xs q-mr-sm" bordered>
                <q-card-section>
                    <div class="text-overline">Follow channel</div>
                    <div class="text-caption">Follow to the selected channel by the link</div>
                    <q-card-section>
                        <q-form class="column justify-center">
                            <q-input v-model="followLink" label="Enter the channel url" hint="https://discord.com/..."
                                     model-value="" class="col col-12 q-mb-sm">
                                <template v-slot:prepend>
                                    <q-icon name="link"/>
                                </template>
                            </q-input>

                            <q-btn outline rounded label="Follow" color="secondary" />
                        </q-form>
                    </q-card-section>
                </q-card-section>
            </q-card>

            <q-card class="col-lg col-xs-12 q-my-xs q-mx-sm" bordered>
                <q-card-section>
                    <div class="text-overline">Unfollow channel</div>
                    <div class="text-caption">Unfollow from selected channel by the link</div>
                    <q-card-section>
                        <q-form class="column justify-center">
                            <q-input v-model="followLink" label="Enter the channel url" hint="https://discord.com/..."
                                     model-value="" class="col col-12 q-mb-sm">
                                <template v-slot:prepend>
                                    <q-icon name="link"/>
                                </template>
                            </q-input>

                            <q-btn outline rounded label="Unfollow" color="secondary" />
                        </q-form>
                    </q-card-section>
                </q-card-section>
            </q-card>

            <q-card class="col-lg col-xs-12 q-my-xs q-ml-sm" bordered>
                <q-card-section>
                    <div class="text-overline">Write a message to the channel</div>
                    <div class="text-caption">Write a custom message to the channel by he link</div>
                    <q-card-section>
                        <q-form class="column justify-center">
                            <q-input v-model="followLink" label="Enter the channel url" hint="https://discord.com/..."
                                     model-value="" class="col col-12 q-mb-sm">
                                <template v-slot:prepend>
                                    <q-icon name="link"/>
                                </template>
                            </q-input>

                            <q-input v-model="followLink" label="Enter the message" hint="Some words..." model-value=""
                                     class="col col-12 q-mb-sm">
                                <template v-slot:prepend>
                                    <q-icon name="link"/>
                                </template>
                            </q-input>

                            <q-btn outline rounded label="Send the message" color="secondary" />
                        </q-form>
                    </q-card-section>
                </q-card-section>
            </q-card>
        </div>

        <q-dialog v-model="confirmDelete">
            <q-card>
                <q-card-section>
                    <span>Do you really wants to delete selected accounts?</span>
                </q-card-section>
                <q-card-actions align="right">
                    <q-btn flat color="negative" label="Yes, I'm sure!" @click="deleteRecords" />
                    <q-btn flat color="secondary" label="Cancel" @click="confirmDelete = false" />
                </q-card-actions>
            </q-card>
        </q-dialog>

    </q-page>
</template>

<script>
import {defineComponent, ref} from 'vue';

const columns = [
    {name: 'usernames', required: true, label: 'Username', align: 'left', field: row => row.username, sortable: true},
    {name: 'emails', required: true, label: 'Email', align: 'left', field: row => row.email, sortable: true},
    {name: 'passwords', required: true, label: 'Password', align: 'left', field: row => row.password},
    {name: 'tokens', required: true, label: 'Token', align: 'left', field: row => row.token},
]

const rows = [
    {id: 1, username: 'Habney1', email: 'stanichgame@gmail.com', password: 'qwerty12345', token: '11rv2ev2323423ew3f10rv2ev2323423ew3f'},
    {id: 2, username: 'Habney2', email: 'stanichgame@gmail.com', password: 'qwerty12345', token: '20rv2ev2323423ew3f11rv2ev2323423ew3f'},
    {id: 3, username: 'Habney3', email: 'stanichgame@gmail.com', password: 'qwerty12345', token: '23rv2ev2323423ew3f11rv2ev2323423ew3f'},
    {id: 4, username: 'Habney4', email: 'stanichgame@gmail.com', password: 'qwerty12345', token: '11rv2ev2323423ew3f11rv2ev2323423ew3f'},
    {id: 5, username: 'Habney4', email: 'stanichgame@gmail.com', password: 'qwerty12345', token: '11rv2ev2323423ew3f11rv2ev2323423ew3f'},
    {id: 6, username: 'Habney4', email: 'stanichgame@gmail.com', password: 'qwerty12345', token: 'rv2ev2323423ew3f1111rv2ev2323423ew3f'},
    {id: 7, username: 'Habney4', email: 'stanichgame@gmail.com', password: 'qwerty12345', token: 'rv2ev2323423ew3f1111rv2ev2323423ew3f'},
    {id: 7, username: 'Habney4', email: 'stanichgame@gmail.com', password: 'qwerty12345', token: 'rv2ev2323423ew3f1111rv2ev2323423ew3f'},
]

export default defineComponent({
    name: 'DiscordIndex',
    methods: {
        clearTableSelection: function (event) {
            this.selected = []
        },
        deleteRecords: function (event) {
            alert('Records has been deleted')
            this.confirmDelete = false
        }
    },
    setup() {
        const selected = ref([])
        const confirmDelete = ref(false)
        const followLink = null

        return {
            columns: columns,
            rows: rows,

            selected: selected,

            confirmDelete: confirmDelete,

            followLink
        }
    },
})
</script>

