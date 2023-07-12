<template>
  <div>


<treeselect

 :multiple="false"
    :options="options"

    v-model="value" @open="handleOpen" @select="handleSelect" value-format="object"  :searchable="searchable" required></treeselect >



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
   props: {

    valueData: {
      type: Object,
      required: true
    },
  },
  data() {

    return {
        value: null,
         searchable: true,

      options: [],
    }
  },
   methods: {
    handleSelect(test) {

    },
    async handleOpen(){
 try {
      const response = await this.$axios.get('/authors');


 this.options = response.data.authors.map(item => ({
            id: item.id,
            label: item.name, // Customize the label property based on the fetched data
          }));



    } catch (error) {
      console.error(error);
    }
    }


  },

   mounted() {
    if(this.valueData.add===true)
    {
       this.value=null;
    }
    else{
this.value= {
          id:this.valueData.author_id,
          label:this.valueData.author_name,
        };
    }


  }
}
</script>
