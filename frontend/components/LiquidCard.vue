<template>
  <v-card elevation="2">
    <v-img height="300" width="300" :src="liquid.url"> </v-img>
    <v-card-title>{{ liquid.title }}</v-card-title>
    <v-select :items="liquid.available" label="Available"></v-select>
      <v-slider
        v-model="value"
        step="10"
        ticks="always"
        tick-size="4"
      >
        <template v-slot:append>
            <v-text-field
                v-model="value"
                class="mt-0 pt-0"
                type="number"
                style="width: 60px"
            ></v-text-field>
        </template>
    </v-slider>
  </v-card>
</template>

<script>
export default {
  props: ['liquid'],
}
</script>

<style scoped>
.e4 {
  width: 400px;
  margin: auto;
}

</style>
