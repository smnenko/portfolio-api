<template>
  <q-page class="justify-start shadow-2">
    <q-tabs inline-label v-model="tab" align="justify">
      <q-tab label="Dashboard" name="dashboard" icon="dashboard" />
      <q-tab label="Add account" name="add_account" icon="create" />
      <q-tab label="Detailed view" name="detailed_view" icon="visibility" />
    </q-tabs>

    <q-tab-panels v-model="tab" animated>
      <q-tab-panel name="dashboard">
        <q-table
          title="Discord accounts"
          :columns="columns"
          :rows="rows"
          selection="multiple"
          v-model:selected="selected"
          :ref="tableRef"
          row-key="id"
        />

        <q-separator class="q-my-lg" />

        <div class="full-width row justify-between">
          <q-card class="col-lg-4 col-xs-12">
            <q-card-section>
              <div class="text-overline">Follow channel</div>
              <div class="text-caption">Follow to the selected channel by the link</div>
              <q-card-section>
                <q-form class="column justify-center">
                  <q-input v-model="followLink" label="Enter the channel url" hint="https://discord.com/..." model-value="" class="col col-12 q-mb-sm">
                    <template v-slot:prepend>
                      <q-icon name="link" />
                    </template>
                  </q-input>

                  <q-btn outline rounded label="Follow" color="warning" class="col col-12" />
                </q-form>
              </q-card-section>
            </q-card-section>
          </q-card>

          <q-card class="col-lg-4 col-xs-12">
            <q-card-section>
              <div class="text-overline">Unfollow channel</div>
              <div class="text-caption">Unfollow from selected channel by the link</div>
              <q-card-section>
                <q-form class="column justify-center">
                  <q-input v-model="followLink" label="Enter the channel url" hint="https://discord.com/..." model-value="" class="col col-12 q-mb-sm">
                    <template v-slot:prepend>
                      <q-icon name="link" />
                    </template>
                  </q-input>

                  <q-btn outline rounded label="Unfollow" color="warning" class="col col-12" />
                </q-form>
              </q-card-section>
            </q-card-section>
          </q-card>

          <q-card class="col-lg-4 col-xs-12">
            <q-card-section>
              <div class="text-overline">Write a message to the channel</div>
              <div class="text-caption">Write a custom message to the channel by he link</div>
              <q-card-section>
                <q-form class="column justify-center">
                  <q-input v-model="followLink" label="Enter the channel url" hint="https://discord.com/..." model-value="" class="col col-12 q-mb-sm">
                    <template v-slot:prepend>
                      <q-icon name="link" />
                    </template>
                  </q-input>

                  <q-input v-model="followLink" label="Enter the message" hint="Some words..." model-value="" class="col col-12 q-mb-sm">
                    <template v-slot:prepend>
                      <q-icon name="link" />
                    </template>
                  </q-input>

                  <q-btn outline rounded label="Send the message" color="warning" class="col col-12" />
                </q-form>
              </q-card-section>
            </q-card-section>
          </q-card>
        </div>
      </q-tab-panel>

      <q-tab-panel name="add_account">
        {{ selected }}
      </q-tab-panel>
    </q-tab-panels>
  </q-page>
</template>

<script>
import {defineComponent, ref} from 'vue';

const columns = [
  {name: 'usernames', required: true, label: 'Username', align: 'left', field: row => row.username, sortable: true},
  {name: 'emails', required: true, label: 'Email', align: 'left', field: row => row.email, sortable: true},
  {name: 'passwords', required: true, label: 'Password', align: 'left', field: row => row.password},
  {name: 'channels', required: true, label: 'Channels', align: 'left', field: row => row.channels, sortable: true},
  {name: 'actions', required: true, label: 'Actions', align: 'left', field: row => null}
]

const rows = [
  {id: 1, username: 'Habney1', email: 'stanichgame@gmail.com', password: 'qwerty12345', channels: 10},
  {id: 2, username: 'Habney2', email: 'stanichgame@gmail.com', password: 'qwerty12345', channels: 20},
  {id: 3, username: 'Habney3', email: 'stanichgame@gmail.com', password: 'qwerty12345', channels: 23},
  {id: 4, username: 'Habney4', email: 'stanichgame@gmail.com', password: 'qwerty12345', channels: 11},
  {id: 5, username: 'Habney4', email: 'stanichgame@gmail.com', password: 'qwerty12345', channels: 11},
  {id: 6, username: 'Habney4', email: 'stanichgame@gmail.com', password: 'qwerty12345', channels: 11},
  {id: 7, username: 'Habney4', email: 'stanichgame@gmail.com', password: 'qwerty12345', channels: 11},
]

export default defineComponent({
  name: 'DiscordIndex',
  data() {

    const selected = ref([])
    const lastIndex = ref(null)
    const tableRef = ref(null)
    const followLink = null

    return {
      columns: columns,
      rows: rows,

      selected: selected,
      lastIndex: lastIndex,
      tableRef: tableRef,

      followLink,

      tab: ref('dashboard')
    }
  },
})
</script>
