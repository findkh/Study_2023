package com.kh.blockmanager;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan("com.kh.blockmanager")
@MapperScan("com.kh.blockmanager.mapper")
public class BlockmanagerApplication {

	public static void main(String[] args) {
		SpringApplication.run(BlockmanagerApplication.class, args);
	}

}
