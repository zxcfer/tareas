package router

import (
	"github.com/gin-gonic/gin"
	"firego/server/controller"
)

type Router struct {
	authController *controller.AuthController
}

func NewRouter(
	authController *controller.AuthController,
) *gin.Engine {
	// Create a new Gin router
	r := gin.Default()

	// Set up the authentication routes
	r.POST("/login", authController.Login)
	r.POST("/register", authController.Register)

	return r
}