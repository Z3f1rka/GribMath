<script setup>
import { onMounted, ref } from 'vue'
import { Input } from './ui/input'
import { Button } from '@/components/ui/button'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import * as z from 'zod'
import router from '@/router'
import axios from 'axios'
import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage
} from '@/components/ui/form'

const formSchema = toTypedSchema(
  z.object({
    username: z
      .string({ required_error: 'Обязательное поле' })
      .min(5, { message: 'Минимум 5 символов' })
      .max(35, { message: 'Максимум 35 символов' }),

    password: z
      .string({ required_error: 'Обязательное поле' })
      .min(5, { message: 'Минимум 5 символов' })
      .max(35, { message: 'Максимум 35 символов' })
  })
)

const baseURL = import.meta.env.VITE_APP_API_URL

const form = useForm({
  validationSchema: formSchema
})

var err = ref('')

const onSubmit = form.handleSubmit((values) => {
  console.log(values)
  axios.post(baseURL + 'login', values).then((response) => {
    err.value = response.data.error
    if (err.value) {
      console.log(err.value)
    } else {
      localStorage.setItem('token', response.data.access_token)
      localStorage.setItem('refresh_token', response.data.refresh_token)
      router.push('/')
    }
  })
})
</script>

<template>
  <div class="dark:text-white">
    <form @submit="onSubmit">
      <FormField v-slot="{ componentField }" name="username">
        <FormItem>
          <FormLabel>Имя пользователя</FormLabel>
          <FormControl>
            <Input type="text" placeholder="Пользователь111" v-bind="componentField" />
          </FormControl>
          <FormMessage />
        </FormItem>
      </FormField>
      <FormField v-slot="{ componentField }" name="password">
        <FormItem>
          <FormLabel>Пароль</FormLabel>
          <FormControl>
            <Input type="password" placeholder="" v-bind="componentField" />
          </FormControl>
          <FormMessage />
        </FormItem>
      </FormField>
      <p>{{ err }}</p>
      <Button type="submit" class="my-8"> Войти </Button>
    </form>
  </div>
</template>
