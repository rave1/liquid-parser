<template>
  <v-row justify="center" align="center">
    <v-col cols="12">
      <v-form ref="form" v-model="valid" lazy-validation>
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
            <v-btn
              color="purple darken-1"
              @click="parse"
              elevation="11"
              :disabled="!valid"
            >
              Submit
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-col>
    <v-alert v-if="error" border="left" type="error"
      >Bitch you need to <nuxt-link to="/login">login</nuxt-link> or
      <nuxt-link to="/regster">register</nuxt-link> first</v-alert
    >
  </v-row>
</template>

<script>
import LiquidCard from '../components/LiquidCard.vue'
import { mapGetters } from 'vuex'
export default {
  components: { LiquidCard },
  name: 'IndexPage',
  data: () => ({
    liquids: [],
    loading: false,
    valid: true,
    error: false,
    urlRules: [
      (v) => !!v || 'URL is required',
      (v) =>
        /^(https?|chrome):\/\/[^\s$.?#].[^\s]*$/.test(v) || 'URL must be valid',
    ],
  }),
  mounted() {
    console.log('cipa')
  },
  computed: {
    ...mapGetters(['isAuthenticated', 'loggedInUser']),
  },
  methods: {
    parse() {
      if (this.$auth.user) {
        console.log(this.url)
        this.loading = true
        this.$refs.form.validate()
        setTimeout(() => (this.loading = false), 2000)
        this.$axios
          .post('http://127.0.0.1:8000/api/parse/', {
            url: this.url,
          })
          .catch((error) => console.log(error))
        this.$axios
          .get('http://127.0.0.1:8000/api/parse')
          .then((res) => (this.liquids = res.data))
      } else {
        this.error = true
      }
    },
  },
}
</script>
