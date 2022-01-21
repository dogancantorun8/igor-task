<template>
    <div id="app">
        <date-picker v-model="mydate" lang="en" type="datetime" format="YYYY-MMMM-DD HH:mm:ss"></date-picker>
        <h1>{{ mydate }}</h1>
        <p>
            <button type="button" @click="save">Submit</button>
        </p>
        <h1>{{ result }}</h1>
    </div>
</template>

<script>
    import DatePicker from 'vue2-datepicker'

    export default {
        name: 'App',
        components: {
            DatePicker
        },
        data() {
            return {
                mydate: '',
                result: {
                    
                    year: '',
                    month: '',
                    day: '',
                    hour: '',
                    minute: '',
                    second: '', 
                }
            }
        },
        methods: {
            save () {
                this.result.year = this.mydate.getFullYear();
                this.result.month = this.mydate.getMonth();
                this.result.day = this.mydate.getDay();
                this.result.hour = this.mydate.getHours();
                this.result.minute = this.mydate.getMinutes();
                this.result.second = this.mydate.getSeconds();
                // or getDate(), getMilliseconds(), getTime()
            }
        }
    }
</script>