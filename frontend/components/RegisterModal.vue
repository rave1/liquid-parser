<template>
  <v-app>
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Register form</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <form ref="form" @submit.prevent="register()">
                  <v-text-field
                    v-model="username"
                    name="username"
                    label="E-mail"
                    :rules="emailRules"
                    placeholder="email"
                    required
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    name="password"
                    label="Password"
                    :rules="passwordRules"
                    type="password"
                    placeholder="password"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="passwordSecond"
                    name="passwordSecond"
                    label="Repeat Password"
                    :rules="passwordRules"
                    type="password"
                    placeholder="password"
                    required
                  ></v-text-field>
                  <v-btn
                    type="submit"
                    class="mt-4"
                    color="primary"
                    value="log in"
                    :disabled="!valid"
                    >Login</v-btn
                  >
                </form>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      passwordSecond: '',
      valid: true,
      emailRules: [
        (v) => !!v || 'E-mail is required',
        (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      passwordRules: [(v) => !!v || 'Password is required'],
    }
  },
  methods: {
    async register() {
      const { username, password, passwordSecond } = this
      try {
        await this.$axios.post('http://127.0.0.1:8000/api/register/', {
          email: username,
          password1: password,
          password2: passwordSecond,
        })

        await this.$auth
          .loginWith('local', {
            data: {
              username: username,
              password: password,
            },
          })
          .then(() => this.$toast.success('Logged In!'))
        this.$router.push('/')
        // .then((res) => this.storeToken(res.data.token))
      } catch (e) {
        console.log(e)
      }
    },
  },
}
</script>
