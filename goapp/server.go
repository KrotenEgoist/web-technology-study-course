package main

import (
	"github.com/SevereCloud/vksdk/api"
	"github.com/gorilla/mux"
	"log"
	"math/rand"
	"net/http"
	"time"
)

func getphoto(w http.ResponseWriter, r *http.Request) {
	token := "TOKEN"
	vk := api.NewVK(token)
	vars := mux.Vars(r)

	ownerId := vars["oid"]
	albumId := vars["aid"]
	var u string
	count, err := vk.PhotosGetAlbums(api.Params{
		"owner_id":  ownerId,
		"album_ids": albumId,
		"count":     1,
	})
	if count.Count == 0 || err != nil {
		u = "Null"
	} else {
		rand.Seed(time.Now().UnixNano())
		n := rand.Intn(count.Items[0].Size)
		photo, err := vk.PhotosGet(api.Params{
			"owner_id": ownerId,
			"album_id": albumId,
			"offset":   n,
			"count":    1,
		})
		if err != nil {
			u = "Null"
		} else {
			u = photo.Items[0].Sizes[len(photo.Items[0].Sizes)-1].URL
		}
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte("{\"img_url\": \"" + u + "\"}"))
	return
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/get/owner_id={oid}&album_id={aid}", getphoto)
	r.PathPrefix("/").Handler(http.FileServer(http.Dir("./static")))
	log.Fatal(http.ListenAndServe("0.0.0.0:5000", r))
}
