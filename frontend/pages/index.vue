<template>
  <v-row justify="center" align="center">
    <v-col cols="12">
      <v-form
      ref="form"
      v-model="valid"
      lazy-validation
      >
        <v-card :loading="loading">
          <v-card-title class="headline"> Paste the link bitch </v-card-title>
          <v-text-field 
            label="URL"
            v-model="url"
            required
            :rules="urlRules"
          ></v-text-field>
          <v-spacer />
          <v-row justify="center" align="center">
            <v-col cols="4" v-for="liquid in liquids" :key="liquid.url">
              <liquid-card :liquid="liquid" />
            </v-col>
          </v-row>
          <v-card-actions>
            <v-spacer />
            <v-btn color="purple darken-1" @click="parse" elevation="11" :disabled="!valid">
              Submit
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-col>
  </v-row>
</template>

<script>
import LiquidCard from '../components/LiquidCard.vue'
export default {
  components: { LiquidCard },
  name: 'IndexPage',
  data: () => ({
    liquids: [],
    loading: false,
    valid: true,
    urlRules: [
      v => !!v || 'URL is required',
      v => /^(https?|chrome):\/\/[^\s$.?#].[^\s]*$/.test(v) || 'URL must be valid'
    ]
  }),
  mounted() {
    console.log('cipa')
  },
  methods: {
    parse() {
      console.log(this.url)
      this.loading = true
      this.$refs.form.validate()
      setTimeout(() => (this.loading = false), 2000)
      this.$axios
        .post('http://127.0.0.1:5000/', {
          url: this.url,
        })
        .catch((error) => console.log(error))
        .then((res) => (this.liquids = res.data))
    },
  },
}
</script>
