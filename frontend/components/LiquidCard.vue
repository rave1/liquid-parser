<template>
  <v-card elevation="2" class="e4">
    <v-img height="300" width="300" :src="liquid.picture"> </v-img>
    <v-card-title>{{ liquid.title }}</v-card-title>
    <v-select :items="liquid.available" label="Available"></v-select>
    <v-card-text>
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <v-slider
              v-model="red"
              :max="20"
              label="Quantity"
              class="align-center"
            >
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
                      <v-btn
              color="purple darken-1"
              @click="addToCart(liquid)"
              elevation="11"
            >
              Add to cart
            </v-btn>
        </v-row>
      </v-container>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  computed: {
    cart(){
      return this.$store.state.shoppingCart
    }
  },
  props: ['liquid'],
  data() {
    return {
      red: 64,
      green: 128,
      blue: 0,
    }
  },
  methods: {
    addToCart(liquid) {
      console.log(this.red)
      const data = {
        id: liquid.id,
        url: liquid.url,
        quantity: this.red
      }
      this.$store.commit('addProductToCart', data)
      this.$toast.success(`${this.red} products added to cart!`).goAway(1500)
      
    }
  }
}
</script>

<style scoped>
.e4 {
  width: 400px;
  margin: auto;
}
</style>
