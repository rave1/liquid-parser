<template>
  <v-card elevation="2" class="e4">
    <v-img height="300" width="300" :src="liquid.url"> </v-img>
    <v-card-title>{{ liquid.title }}</v-card-title>
    <v-select :items="liquid.available" label="Available"></v-select>
    <v-card-text>
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <v-slider v-model="red" :max="20" label="R" class="align-center">
              <template v-slot:append>
                <v-text-field
                  v-model="red"
                  class="mt-0 pt-0"
                  type="number"
                  style="width: 60px"
                ></v-text-field>
              </template>
            </v-slider>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: ['liquid'],
  data() {
    return {
      red: 64,
      green: 128,
      blue: 0,
    }
  },
}
</script>

<style scoped>
.e4 {
  width: 400px;
  margin: auto;
}
</style>
