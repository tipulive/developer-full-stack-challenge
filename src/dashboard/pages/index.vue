<template>
  <div>
<h1>Home</h1>
    <div class="container">
<treeselect

 :multiple="false"
    :options="options"

    v-model="value" @open="handleOpen" @select="handleSelect" value-format="object"  :searchable="searchable"></treeselect >

    </div>

  </div>
</template>

<script>
 import Treeselect from '@riophae/vue-treeselect'
  // import the styles
  import '@riophae/vue-treeselect/dist/vue-treeselect.css'
export default {
    components: {
    Treeselect,
  },
  data() {
    return {
        value: {
          id: 'a',
          label: 'a',
        },
         searchable: true,

      options: [],
    }
  },
   methods: {
    handleSelect(test) {
      console.log(test.id);
    },
    handleOpen(){

    }


  },

   async mounted() {
    try {

      const response = await this.$axios.get('/books');
      //this.options = response.data;
      this.options = response.data.map(item => ({
            id: item.id,
            label: item.name, // Customize the label property based on the fetched data
          }));

       console.log(response.data);


    } catch (error) {
      console.error(error);
    }
  }
}
</script>
