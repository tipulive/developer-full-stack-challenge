
<template>
  <div class="p-4">


<b-container >
 <b-form-group>
      <b-form-input v-model="searchQuery"  placeholder="Search by name" @input="searchAuthors" />
    </b-form-group>
    <div class="text-right mb-3">
    <b-button size="sm" variant="primary" @click="addAuthor()">
          Add New
        </b-button>
  </div>
 <b-table striped hover :items="authors" :fields="tableFields" @row-clicked="ViewAuthor">

    <template v-slot:cell(actions)="data" v-if="showSearch">
        <b-button size="sm" variant="primary" >
          Edit
        </b-button>
        <b-button size="sm" variant="danger" @click="deleteAuthor(data.item)">
          Delete
        </b-button>
      </template>
 </b-table>
 <div class="text-center">
        <button @click="previousPage" :disabled="page === 1">Previous</button>
      <button @click="nextPage" :disabled="authors.length < limit">Next</button>
 </div>
</b-container>
<AuthorAddModal/>
<AuthorEditModal/>

  </div>
</template>

<script>
import AuthorAddModal from '@/components/Authors/AuthorAddModal.vue';
import AuthorEditModal from '@/components/Authors/AuthorEditModal.vue';
export default {
    components: {
    AuthorAddModal,
    AuthorEditModal
  },
  data() {
    return {
        showSearch:false,
      //authors: [],
      propAuthor: {},
      OpenModal:false,
      authName:"",
      searchQuery:"",
      page: 1,
      limit: 10,
      showCompValue:false,
    bookFieldData:[
       { key: 'name', label: 'Name' },
       { key: 'pages', label: 'pages' },
       "actions"

      ],
      tableFields:[

       { key: 'name', label: 'Name' },
       { key: 'book_count', label: 'Number of books' },


      ],
        sortBy: 'name',
      sortDesc: false
    };
  },
  mounted() {
    this.fetchAuthors();
  },
  computed: {
    authors() {
      return this.$store.state.author.authorData;
    }
  },
  methods: {
    async fetchAuthors() {
 const payload = {
        page:this.page,
        limit:this.limit,
        search:this.searchQuery,
        sort:'desc',
      };

await this.$store.dispatch('author/fetchAuthors',payload)

      //this.authors=this.$store.state.author.authorData


    },
    searchAuthors() {
        this.OpenModal=false;
      this.page = 1;
      this.fetchAuthors();
    },
    previousPage() {
      this.page--;
      this.fetchAuthors();
    },
    nextPage() {
      this.page++;
      this.fetchAuthors();
    },
     addAuthor() {
    this.$bvModal.show('authorAdd-modal');

      // Handle the logic to open the modal for editing the author
    },

     async ViewAuthor(author) {
        console.log(author.id)
         const payload = {
        id:author.id,
        name:author.name,


      };
        this.$bvModal.show('authorEdit-modal');
         await this.$store.dispatch('author/updateAuthorPass',payload)


      // Handle the logic to open the modal for editing the author
    },
    deleteAuthor(author) {
      // Handle the logic to delete the author
    }
  }
};
</script>
